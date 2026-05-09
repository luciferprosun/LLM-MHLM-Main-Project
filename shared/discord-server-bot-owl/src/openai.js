import { config } from "./config.js";

const OPENAI_URL = "https://api.openai.com/v1/responses";
const OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions";

export async function askOpenAI(prompt, options = {}) {
  const systemPrompt = options.systemPrompt || config.aiSystemPrompt;

  if (config.openrouterApiKey) {
    return askOpenRouter(prompt, systemPrompt);
  }

  if (!config.openaiApiKey) {
    throw new Error("Missing OPENROUTER_API_KEY or OPENAI_API_KEY in .env");
  }

  const response = await fetch(OPENAI_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${config.openaiApiKey}`
    },
    body: JSON.stringify({
      model: config.openaiModel,
      input: [
        {
          role: "system",
          content: systemPrompt
        },
        {
          role: "user",
          content: prompt
        }
      ]
    })
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`OpenAI API error ${response.status}: ${body}`);
  }

  const data = await response.json();
  const text = String(data.output_text || "").trim();
  if (!text) {
    throw new Error("OpenAI returned an empty response.");
  }

  return text;
}

async function askOpenRouter(prompt, systemPrompt) {
  const primaryModel = config.openrouterModel;
  try {
    return await sendOpenRouterRequest(prompt, systemPrompt, primaryModel);
  } catch (error) {
    const fallbackModel = config.openrouterFallbackModel;
    const shouldFallback =
      fallbackModel &&
      fallbackModel !== primaryModel &&
      /OpenRouter API error 429:/.test(String(error?.message || error));

    if (!shouldFallback) {
      throw error;
    }

    return sendOpenRouterRequest(prompt, systemPrompt, fallbackModel);
  }
}

async function sendOpenRouterRequest(prompt, systemPrompt, model) {
  const response = await fetch(OPENROUTER_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${config.openrouterApiKey}`
    },
    body: JSON.stringify({
      model,
      messages: [
        {
          role: "system",
          content: systemPrompt
        },
        {
          role: "user",
          content: prompt
        }
      ]
    })
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`OpenRouter API error ${response.status}: ${body}`);
  }

  const data = await response.json();
  const text = String(data.choices?.[0]?.message?.content || "").trim();
  if (!text) {
    throw new Error("OpenRouter returned an empty response.");
  }

  return text;
}

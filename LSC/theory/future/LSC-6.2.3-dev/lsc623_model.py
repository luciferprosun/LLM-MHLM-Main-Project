import numpy as np

def lsc_response(E, t, n_vec, lambda_0, lambda_A, A_tensor, f0, fA):
    """
    Effective LSC 6.2.3 detector-frame response modifier.

    Parameters
    ----------
    E : float or ndarray
        Neutrino energy.
    t : float or ndarray
        Time variable.
    n_vec : ndarray
        Unit direction vector in detector coordinates, shape (..., 3).
    lambda_0 : float
        Isotropic trace-response amplitude.
    lambda_A : float
        Traceless anisotropic response amplitude.
    A_tensor : ndarray
        Symmetric traceless 3x3 tensor.
    f0 : callable
        Isotropic response function f0(E, t).
    fA : callable
        Anisotropic response function fA(E, t).

    Returns
    -------
    modifier : float or ndarray
        Multiplicative detector-response correction.
    """

    A_tensor = np.asarray(A_tensor)

    # enforce trace check but do not silently modify the model
    trace_A = np.trace(A_tensor)
    if abs(trace_A) > 1e-10:
        raise ValueError("A_tensor must be traceless for LSC 6.2.3.")

    n_vec = np.asarray(n_vec)

    anisotropic_projection = np.einsum("...i,ij,...j->...", n_vec, A_tensor, n_vec)

    modifier = 1.0 + lambda_0 * f0(E, t) + lambda_A * anisotropic_projection * fA(E, t)

    return modifier


def predicted_events(N0, E, t, n_vec, lambda_0, lambda_A, A_tensor, f0, fA):
    """
    Apply the LSC 6.2.3 response modifier to a baseline prediction.
    """
    return N0 * lsc_response(E, t, n_vec, lambda_0, lambda_A, A_tensor, f0, fA)


def residual(N_obs, N0):
    """
    Fractional residual relative to the baseline model.
    """
    return (N_obs - N0) / N0


def lsc_residual_model(E, t, n_vec, lambda_0, lambda_A, A_tensor, f0, fA):
    """
    Residual form of the LSC 6.2.3 response model.
    """
    A_tensor = np.asarray(A_tensor)

    if abs(np.trace(A_tensor)) > 1e-10:
        raise ValueError("A_tensor must be traceless.")

    anisotropic_projection = np.einsum("...i,ij,...j->...", n_vec, A_tensor, n_vec)

    return lambda_0 * f0(E, t) + lambda_A * anisotropic_projection * fA(E, t)

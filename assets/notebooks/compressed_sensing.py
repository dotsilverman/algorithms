import numpy as np
import matplotlib.pyplot as plt
import plot_tools as pt
import scipy as sci
pt.matplotlib_header()

def gen_rand_signal(size,rho0):
  """ Generate a random sparse vector of size 'size', with 'rho0' ratio of
  nonzero values. """
  nonzeros = np.random.randint(0,size,size=int(round(size*rho0)))
  vec = np.zeros(size)
  for nonzero in nonzeros:
    vec[nonzero] = np.random.randn()
  #vec /= (vec**2).sum()**0.5
  return vec

def setup_linprog(basis_change,measurements):
  """ Generate compressed sensing input for a linear program solver. """
  num_measurements = basis_change.shape[0]
  signal_size = basis_change.shape[1]
  coefs = np.ones(2*signal_size)
  coefs[:signal_size] = 0.
  ineq_mat = np.identity(2*signal_size)
  ineq_mat[signal_size:,signal_size:] = -np.identity(signal_size)
  ineq_mat[:signal_size,signal_size:] = -np.identity(signal_size)
  ineq_mat[signal_size:,:signal_size] = -np.identity(signal_size)
  eq_mat = np.zeros((2*signal_size,2*signal_size))
  eq_mat[:num_measurements,:signal_size] = basis_change
  eq_vec = np.zeros(2*signal_size)
  eq_vec[:num_measurements] = measurements
  return coefs,ineq_mat,eq_mat,eq_vec

def test_leastsquares(signal_size,frac_measurements,signal_sparsity):
  """ Run least squares fitting of measurement data and check error. """
  num_measurements = int(round(frac_measurements * signal_size))
  signal_size = int(round(signal_size))
  signal = gen_rand_signal(signal_size,signal_sparsity)
  basis_change = np.random.randn(num_measurements,signal_size)/signal_size
  measurements = np.dot(basis_change,signal)
  estimate,_,_,_ = np.linalg.lstsq(basis_change,measurements)
  return np.linalg.norm(estimate-signal,2) / np.linalg.norm(signal,2)

def plot_linprog(signal_size,frac_measurements,signal_sparsity,ax):
  """ Run least squares fitting of measurement data and check error. """
  num_measurements = int(round(frac_measurements * signal_size))
  signal_size = int(round(signal_size))
  signal = gen_rand_signal(signal_size,signal_sparsity)
  ax[0].bar(range(len(signal)),signal)
  basis_change = np.random.randn(num_measurements,signal_size)/signal_size
  measurements = np.dot(basis_change,signal)
  coefs,ineq_mat,eq_mat,eq_vec = setup_linprog(basis_change,measurements)
  result = sci.optimize.linprog(
      coefs,
      ineq_mat,
      np.zeros(2*signal_size),
      eq_mat,
      eq_vec,
      bounds=[(-np.inf,np.inf) for var in eq_vec],
      options={'maxiter':10000} )
  if result['message'] != 'Optimization terminated successfully.':
    estimate = np.nan
  else:
    estimate = result['x'][:signal_size]
  ax[1].bar(range(len(estimate)),estimate)
  return np.linalg.norm(estimate-signal,2) / np.linalg.norm(signal,2)

def plot_linprog_const(signal_size,frac_measurements,signal,ax):
  """ Run least squares fitting of measurement data and check error. Hold signal
  constant."""
  num_measurements = int(round(frac_measurements * signal_size))
  signal_size = int(round(signal_size))
  #signal = gen_rand_signal(signal_size,signal_sparsity)
  ax[0].bar(range(len(signal)),signal)
  basis_change = np.random.randn(num_measurements,signal_size)/signal_size
  measurements = np.dot(basis_change,signal)
  coefs,ineq_mat,eq_mat,eq_vec = setup_linprog(basis_change,measurements)
  result = sci.optimize.linprog(
      coefs,
      ineq_mat,
      np.zeros(2*signal_size),
      eq_mat,
      eq_vec,
      bounds=[(-np.inf,np.inf) for var in eq_vec],
      options={'maxiter':10000} )
  if result['message'] != 'Optimization terminated successfully.':
    estimate = np.nan
  else:
    estimate = result['x'][:signal_size]
  ax[1].bar(range(len(estimate)),estimate)
  return np.linalg.norm(estimate-signal,2) / np.linalg.norm(signal,2)

def test_linprog(signal_size,frac_measurements,signal_sparsity):
  """ Run least squares fitting of measurement data and check error. """
  num_measurements = int(round(frac_measurements * signal_size))
  signal_size = int(round(signal_size))
  signal = gen_rand_signal(signal_size,signal_sparsity)
  basis_change = np.random.randn(num_measurements,signal_size)/signal_size
  measurements = np.dot(basis_change,signal)
  coefs,ineq_mat,eq_mat,eq_vec = setup_linprog(basis_change,measurements)
  result = sci.optimize.linprog(
      coefs,
      ineq_mat,
      np.zeros(2*signal_size),
      eq_mat,
      eq_vec,
      bounds=[(-np.inf,np.inf) for var in eq_vec],
      options={'maxiter':10000} )
  if result['message'] != 'Optimization terminated successfully.':
    estimate = np.nan
  else:
    estimate = result['x'][:signal_size]
  return np.linalg.norm(estimate-signal,2) / np.linalg.norm(signal,2)

def test_linearprog(signal_size,frac_measurements,signal_sparsity):
  num_measurements = int(round(frac_measurements * signal_size))
  signal_size = int(round(signal_size))
  signal = gen_rand_signal(signal_size,signal_sparsity)
  basis_change = np.random.randn(num_measurements,signal_size)/signal_size
  measurements = np.dot(basis_change,signal)
  estimate,_,_,_ = np.linalg.lstsq(basis_change,measurements)
  return np.linalg.norm(estimate-signal) / np.linalg.norm(signal)

def sample_image(im_arr,rho0):
  """ Take rho0 samples from image randomly. """
  samples = np.zeros(im_arr.shape)
  nget = int(round(rho0*im_arr.flatten().shape[0]))
  xs = np.random.randint(0,im_arr.shape[0],nget)
  ys = np.random.randint(0,im_arr.shape[1],nget)
  for coord in zip(xs,ys):
    samples[coord] = im_arr[coord]
  return samples

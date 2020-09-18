# -*- coding: utf-8 -*-
"""
pysteps.postprocessing.DA.enKF

More to come...
====================================

Calculate assimilated results based on KalmanFilter with fusion of NWP data

Prequisites:
  -filterpy

"""
import numpy as np
from filterpy.kalman import EnsembleKalmanFilter as EnKF
from filterpy.kalman import KalmanFilter

def enKF(X,Z,time_spacing):
  '''
  Parameters
    ----------

    X : numpy-array (member, time, height, width)
        Extrapolated radar derived rainfall fields

    Z : numpy-array (member, time, height, width)
        NWP-based measurements

    time_spacing : int
        Indicate how frequent the NWP data is available to fuse

    cl : float 
        confidence level to compute the uncertainty

    {extra_kwargs_doc}

    Returns
    -------

    estimates : numpy-array (time, height, width)
        The best estimator from the assimilation

    upper_estimates : numpy-array (time, height, width)
        The upper limit of the estimates based on defined confidence level

    lower_estimates : numpy-array (time, height, width)
        The lower limit of the estimates based on defined confidence level

  '''

  def hx(x):
    return np.array([x[0]])

  def fx(x, dt):
      '''Update function, here we use extrapolated function'''
      return x[int(dt)+1]

  mem, t, rows, cols= X.shape


  # initialize noise


  estimates= np.zeros((t, rows, cols)) * np.nan
  upper_estimates= np.zeros((t, rows, cols)) * np.nan
  lower_estimates= np.zeros((t, rows, cols)) * np.nan

  for m in range(rows):
    for n in range(cols):
      P = np.eye(mem) * 100.
      x= X[:,0,m,n]
      enf = EnKF(x=x, P=P, dim_z=1, dt=1., N=10, hx=hx, fx=fx)
      std_noise = 10.
      enf.R *= std_noise**2
      zs= []
      for it in range(t-1):
        if it%10==0:
          z= Z[t//10,m,n]
          zs.append(z)
        enf.predict()
        enf.update(np.asarray([z]))
        estimates[it,m,n]=(enf.x[0])
        upper_estimates[it,m,n]= enf.x[0] + 3*(enf.P[0,0]**.5)
        lower_estimates[it,m,n]= enf.x[0] + 3*(enf.P[0,0]**.5)

  return estimates, upper_estimates, lower_estimates
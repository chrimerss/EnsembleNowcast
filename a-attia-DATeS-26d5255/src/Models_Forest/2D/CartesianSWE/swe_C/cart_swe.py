
"""
============================================================================================
=                                                                                          =
=   DATeS: Data Assimilation Testing Suite.                                                =
=                                                                                          =
=   Copyright (C) 2016  A. Sandu, A. Attia, P. Tranquilli, S.R. Glandon,                   =
=   M. Narayanamurthi, A. Sarshar, Computational Science Laboratory (CSL), Virginia Tech.  =
=                                                                                          =
=   Website: http://csl.cs.vt.edu/                                                         =
=   Phone: 540-231-6186                                                                    =
=                                                                                          =
=   This program is subject to the terms of the Virginia Tech Non-Commercial/Commercial    =
=   License. Using the software constitutes an implicit agreement with the terms of the    =
=   license. You should have received a copy of the Virginia Tech Non-Commercial License   =
=   with this program; if not, please contact the computational Science Laboratory to      =
=   obtain it.                                                                             =
=                                                                                          =
============================================================================================
"""

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _cart_swe.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cart_swe', [dirname(__file__)])
        except ImportError:
            import _cart_swe
            return _cart_swe
        if fp is not None:
            try:
                _mod = imp.load_module('_cart_swe', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cart_swe = swig_import_helper()
    del swig_import_helper
else:
    import _cart_swe
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def new_doublep():
    return _cart_swe.new_doublep()
new_doublep = _cart_swe.new_doublep

def copy_doublep(value):
    return _cart_swe.copy_doublep(value)
copy_doublep = _cart_swe.copy_doublep

def delete_doublep(obj):
    return _cart_swe.delete_doublep(obj)
delete_doublep = _cart_swe.delete_doublep

def doublep_assign(obj, value):
    return _cart_swe.doublep_assign(obj, value)
doublep_assign = _cart_swe.doublep_assign

def doublep_value(obj):
    return _cart_swe.doublep_value(obj)
doublep_value = _cart_swe.doublep_value

def new_intp():
    return _cart_swe.new_intp()
new_intp = _cart_swe.new_intp

def copy_intp(value):
    return _cart_swe.copy_intp(value)
copy_intp = _cart_swe.copy_intp

def delete_intp(obj):
    return _cart_swe.delete_intp(obj)
delete_intp = _cart_swe.delete_intp

def intp_assign(obj, value):
    return _cart_swe.intp_assign(obj, value)
intp_assign = _cart_swe.intp_assign

def intp_value(obj):
    return _cart_swe.intp_value(obj)
intp_value = _cart_swe.intp_value

def new_darray(nelements):
    return _cart_swe.new_darray(nelements)
new_darray = _cart_swe.new_darray

def delete_darray(ary):
    return _cart_swe.delete_darray(ary)
delete_darray = _cart_swe.delete_darray

def darray_getitem(ary, index):
    return _cart_swe.darray_getitem(ary, index)
darray_getitem = _cart_swe.darray_getitem

def darray_setitem(ary, index, value):
    return _cart_swe.darray_setitem(ary, index, value)
darray_setitem = _cart_swe.darray_setitem

def model_init(mesh_size, thread_count, initial_cond):
    return _cart_swe.model_init(mesh_size, thread_count, initial_cond)
model_init = _cart_swe.model_init

def model_del():
    return _cart_swe.model_del()
model_del = _cart_swe.model_del

def model_rhs(t, in_vector, out_vector):
    return _cart_swe.model_rhs(t, in_vector, out_vector)
model_rhs = _cart_swe.model_rhs

def model_jac_vec(t, in_state, in_vector, out_vector):
    return _cart_swe.model_jac_vec(t, in_state, in_vector, out_vector)
model_jac_vec = _cart_swe.model_jac_vec

def model_jac_t_vec(t, in_state, in_vector, out_vector):
    return _cart_swe.model_jac_t_vec(t, in_state, in_vector, out_vector)
model_jac_t_vec = _cart_swe.model_jac_t_vec

def vec_init():
    return _cart_swe.vec_init()
vec_init = _cart_swe.vec_init

def vec_del(in_vector):
    return _cart_swe.vec_del(in_vector)
vec_del = _cart_swe.vec_del

def vec_get_size(out_integer):
    return _cart_swe.vec_get_size(out_integer)
vec_get_size = _cart_swe.vec_get_size

def vec_scale(in_alpha, io_vector):
    return _cart_swe.vec_scale(in_alpha, io_vector)
vec_scale = _cart_swe.vec_scale

def vec_copy(in_vector, out_vector):
    return _cart_swe.vec_copy(in_vector, out_vector)
vec_copy = _cart_swe.vec_copy

def vec_dot(in_vector_x, in_vector_y, out_scalar):
    return _cart_swe.vec_dot(in_vector_x, in_vector_y, out_scalar)
vec_dot = _cart_swe.vec_dot

def vec_axpy(in_alpha, in_vector_x, io_vector_y):
    return _cart_swe.vec_axpy(in_alpha, in_vector_x, io_vector_y)
vec_axpy = _cart_swe.vec_axpy

def vec_add(in_vector_x, io_vector_y):
    return _cart_swe.vec_add(in_vector_x, io_vector_y)
vec_add = _cart_swe.vec_add

def vec_norm2(in_vector, out_scalar):
    return _cart_swe.vec_norm2(in_vector, out_scalar)
vec_norm2 = _cart_swe.vec_norm2


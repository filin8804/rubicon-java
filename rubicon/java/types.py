from ctypes import *

__all__ = [
    'jboolean', 'jbyte', 'jchar', 'jshort', 'jint', 'jlong', 'jfloat', 'jdouble',
    'jsize',
    'jobject', 'jmethodID', 'jfieldID',
    'jclass', 'jthrowable', 'jstring', 'jarray',
    'jbooleanArray', 'jbyteArray', 'jcharArray', 'jshortArray', 'jintArray', 'jlongArray', 'jfloatArray', 'jdoubleArray', 'jobjectArray',
]

jboolean = c_bool
jbyte = c_byte
jchar = c_wchar
jshort = c_short
jint = c_int
jlong = c_long
jfloat = c_float
jdouble = c_double

jboolean_p = POINTER(jboolean)
jbyte_p = POINTER(jbyte)
jchar_p = POINTER(jchar)
jshort_p = POINTER(jshort)
jint_p = POINTER(jint)
jlong_p = POINTER(jlong)
jfloat_p = POINTER(jfloat)
jdouble_p = POINTER(jdouble)

jsize = jint

jobject = c_void_p

jmethodID = c_void_p
jfieldID = c_void_p

jclass = jobject
jthrowable = jobject
jstring = jobject
jarray = jobject
jbooleanArray = jarray
jbyteArray = jarray
jcharArray = jarray
jshortArray = jarray
jintArray = jarray
jlongArray = jarray
jfloatArray = jarray
jdoubleArray = jarray
jobjectArray = jarray

DISPATCH_FUNCTION = CFUNCTYPE(None, c_char_p, c_char_p, c_int, POINTER(c_void_p))

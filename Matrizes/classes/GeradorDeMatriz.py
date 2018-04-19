# -*- coding: utf-8 -*-

from classes.Matriz import Matriz
from classes.MatrizQuadrada import MatrizQuadrada


def e_quadrada(mat):
    """Retorna true sse mat for quadrada."""
    return len(mat) == len(mat[0])


def e_simetrica(mat):
    """Retorna true sse mat for simétrica."""

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j] != mat[j][i]):
                return False
    return True


def e_triangular_inferior(mat):
    """Retorna true sse mat for triangular inferior."""

    for i in range(len(mat)):
        for j in range(i+1, len(mat[0])):
            if mat[i][j] != 0:
                return False
    return True


def e_triangular_superior(mat):
    """Retorna true sse a matriz for triangular superior."""

    for j in range(len(mat)):
        for i in range(j+1, len(mat)):
            if mat[i][j] != 0:
                return False
    return True


def cria_matriz(mat):
    """Avalia mat e cria a matriz adequada às suas características."""

    if e_quadrada(mat):

        if e_simetrica(mat):
            return MatrizQuadrada(mat, simetrica=True)
        if e_triangular_inferior(mat):
            return MatrizQuadrada(mat, triang_inf=True)
        if e_triangular_superior(mat):
            return MatrizQuadrada(mat, triang_sup=True)

        return MatrizQuadrada(mat)

    else:
        return Matriz(mat)

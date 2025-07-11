while np.abs(Pobj.value - Fobj.value) > 1e-6:
    ztil.value = np.abs(z.value)
    Pprob.solve()
    rtil.value = cp.vstack(r).value
    Fprob.solve()
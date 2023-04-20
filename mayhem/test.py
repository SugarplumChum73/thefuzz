#!/usr/bin/python3
import sys
import atheris

with atheris.instrument_imports():
    from thefuzz import fuzz

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    str_1_len = fdp.ConsumeIntInRange(0, 100)
    str_2_len = fdp.ConsumeIntInRange(0, 100)

    str_1 = fdp.ConsumeString(str_1_len)
    str_2 = fdp.ConsumeString(str_2_len)

    fuzz.ratio(str_1, str_2)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires

base = python_requires("boost_base/1.69.0@bincrafters/testing")


class BoostParameterConan(base.BoostBaseConan):
    name = "boost_parameter"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_parameter"
    lib_short_names = ["parameter"]
    header_only_libs = ["parameter"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_mpl",
        "boost_optional",
        "boost_preprocessor",
        "boost_type_traits",
        "boost_utility"
    ]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostParameterConan(base.BoostBaseConan):
    name = "boost_parameter"
    url = "https://github.com/bincrafters/conan-boost_parameter"
    lib_short_names = ["parameter"]
    header_only_libs = ["parameter"]
    options = {"with_boost_python": [True, False]}
    default_options = "with_boost_python=False"
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_mpl",
        "boost_optional",
        "boost_preprocessor",
        "boost_python",
        "boost_type_traits",
        "boost_utility"
    ]

    def requirements_additional(self):
        if self.options.with_boost_python:
            self.requires("boost_python/1.67.0@bincrafters/testing")

    def package_info_additional(self):
        if self.options.with_boost_python:
            self.info.options["boost_python"].python_version = "any"

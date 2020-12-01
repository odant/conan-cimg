# CImg Conan package
# Dmitriy Vetutnev, Odant, 2020


from conans import ConanFile


class CImgConan(ConanFile):
    name = "cimg"
    version = "2.9.4"
    license = "CImg is a free, open-source library distributed under the CeCILL-C (close to the GNU LGPL) or CeCILL (compatible with the GNU GPL) licenses. It can be used in commercial applications."
    description = "The CImg Library is a small and open-source C++ toolkit for image processing http://cimg.eu"
    url = "https://github.com/odant/conan-cimg"
    exports_sources = "src/CImg.h", "src/plugins/*"
    no_copy_source = True

    def package(self):
        self.copy("CImg.h", src="src", dst="include")
        self.copy("*.h", src="src/plugins", dst="include/plugins")

    def package_id(self):
        self.info.header_only()


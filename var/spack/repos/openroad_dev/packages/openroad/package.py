from spack.package import *


class Openroad(CMakePackage):
    """OpenROAD is an open-source application implementing an RTL-to-GDS flow,
    enabling the autonomous digital layout generation directly from RTL code."""

    homepage = "https://github.com/The-OpenROAD-Project/OpenROAD"
    git = "https://github.com/The-OpenROAD-Project/OpenROAD.git"

    #version("latest", git = "https://github.com/The-OpenROAD-Project/OpenROAD.git", branch="master", submodules=True)
    
    version("dev", url="file:///<local_tar_path>",
            sha256="<sha256_of_the_tar_file>")
    version("2.0-19635", commit="ee547ca5bc8fbcaeb199f6879a9f4ea566432df9", submodules=True)
    
    depends_on("cmake@3.24:", type="build")
    depends_on("ninja", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("swig@4:", type="build")
    depends_on("pkgconfig", type="build")
    
    
    ## qt
    depends_on("qt")
    
    boost_options = ("+iostreams", "+test", "+serialization", "+system", "+thread")
    depends_on("boost@1.86: {0}".format(" ".join(boost_options)))
    depends_on("eigen@3.4:")
    depends_on("cudd")
    depends_on("tcl")
    depends_on("tcl-tcllib")
    depends_on("readline")
    depends_on("tclreadline")
    depends_on("python@3.11:")
    depends_on("spdlog")
    depends_on("libffi")
    depends_on("llvm")
    depends_on("lemon")
    depends_on("or-tools@9.11:")
    depends_on("glpk")
    depends_on("zlib")
    depends_on("clp")
    depends_on("cbc")
    depends_on("re2")
    depends_on("googletest")

    variant("gui", default=True, description="Build with GUI")



class CMakeBuilder(spack.build_systems.cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            "-DCMAKE_BUILD_TYPE=RELEASE",
            "-DCMAKE_INSTALL_PREFIX={0}".format(self.spec.prefix),
            "-Dbison_ROOT={0}".format(self.spec["bison"].prefix),
            "-DSWIG_ROOT={0}".format(self.spec["swig"].prefix),
            "-DBoost_ROOT={0}".format(self.spec["boost"].prefix),
            "-DEigen3_ROOT={0}".format(self.spec["eigen"].prefix),
            "-DLEMON_ROOT={0}".format(self.spec["lemon"].prefix),
            "-Dspdlog_ROOT={0}".format(self.spec["spdlog"].prefix),
            "-DGTest_ROOT={0}".format(self.spec["googletest"].prefix),
            "-Dortools_ROOT={0}".format(self.spec["or-tools"].prefix),

        ]
        
        if "+gui" in self.spec:
            args.append("-DBUILD_GUI=ON")
        else:
            args.append("-DBUILD_GUI=OFF")  

        
        return args


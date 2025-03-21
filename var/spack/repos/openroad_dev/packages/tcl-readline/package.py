from spack.package import *

class Tclreadline(AutotoolsPackage):
    """
    tclreadline is a readline extension for tcl shells.
    """

    homepage = "https://github.com/flightaware/tclreadline"
    url      = "https://github.com/flightaware/tclreadline/archive/refs/tags/v2.4.1.tar.gz"
    git      = "https://github.com/flightaware/tclreadline.git"
   
    version("2.4.1",  sha256="d14b1568b6db8cd51659e3cc476a1f45da2020434ebb90b4b0defbc424f05907")
    
    depends_on("tcl")
    depends_on("readline")
    depends_on("tk")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    variant('tclshrl', default=False, description='Build with tclshrl')
    variant('wishrl', default=False, description='Build with wishrl')


    def configure_args(self):
        spec = self.spec
        args = [
            "--with-tcl={0}".format(spec["tcl"].prefix.lib),
            "--with-readline={0}".format(spec["readline"].prefix.lib),
            "--with-tk={0}".format(spec["tk"].prefix.lib),
            "--with-readline-includes={0}".format(spec["readline"].prefix.include)
        ]

        # optional
        if "+tclshrl" in spec:
            args.append("--enable-tclshrl")
        if "+wishrl" in spec:
            args.append("--enable-wishrl")

        return args 
    
    def autoreconf(self, spec, prefix):
        sh = which("sh")
        sh("autogen.sh",extra_env={"NOCONFIGURE":"1"})
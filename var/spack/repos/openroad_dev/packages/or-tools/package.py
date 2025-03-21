from spack.package import *

class OrTools(Package):
    """OR-Tools 9.11.4201 for OpenROAD"""

    homepage = "https://github.com/google/or-tools"
    url = "https://github.com/google/or-tools.git"
    
    version("9.11.4201-cpp-ubuntu-22.04", url="https://github.com/google/or-tools/releases/download/v9.11/or-tools_amd64_ubuntu-22.04_cpp_v9.11.4210.tar.gz", 
            sha256="f613574d4eae01afd966c8bde199990cbd9fad46035e675d71f17f5c7477eed4")

    def install(self, spec, prefix):
        tar = which("tar")
        tar("-xvf", self.stage.archive_file)
        install_tree("or-tools_x86_64_Ubuntu-22.04_cpp_v9.11.4210", prefix)
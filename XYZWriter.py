# Copyright (c) 2017 Jerry Kotas
# XYZWriter is released under the terms of the AGPLv3 or higher.

import io
import subprocess
import tempfile
import os

from UM.Mesh.MeshWriter import MeshWriter
from UM.Logger import Logger
from UM.Application import Application
import UM.PluginRegistry  # To get the g-code writer plug-in to obtain the g-code for us.
import UM.Platform

class XYZWriter(MeshWriter):
    def __init__(self):
        super().__init__()

    def write(self, stream, nodes, mode = MeshWriter.OutputMode.TextMode):
        """
        Write the 3w data to a stream.

        Inputs: stream - The stream to write to.
                nodes - Ignored.
                mode - Ignored.
        Output: Success or Failure
        """
        # Get the g-code.
        try:
                stringio = io.StringIO()
                UM.PluginRegistry.PluginRegistry.getInstance().getPluginObject("GCodeWriter").write(stringio, None)
                stringio.seek(0)
                gcode_data = stringio.read()
                temp_gcode = tempfile.NamedTemporaryFile("w", delete=False)
                temp_gcode.write(gcode_data)
                temp_gcode.close()
        except EnvironmentError as e:
                if temp_gcode:
                        Logger.log("e", "Error writing temporary g-code file {file_name}: {error_msg}".format(file_name=temp_gcode.name, error_msg=str(e)))
                        os.remove(temp_gcode.name)
                else:  # The NamedTemporaryFile constructor failed.
                        Logger.log("e", "Error creating temporary g-code file: {error_msg}".format(error_msg=str(e)))
                return False

        # Check if threedub is callable
        try:
            subprocess.check_output(['threedub', '-h'])
        except Exception as e:
            Logger.log("e", "threedub could not be called: %s", str(e))
            os.remove(temp_gcode.name)
            return False

        # Call the converter application to convert it to 3w.
        cmd = ['threedub', temp_gcode.name, stream.name]
        try:
            subprocess.check_output(cmd)
        except Exception as e:
            Logger.log("e", "System call to threedub failed: %s", str(e))
            os.remove(temp_gcode.name)
            return False

        # Clean Up
        os.remove(temp_gcode.name)
        return True

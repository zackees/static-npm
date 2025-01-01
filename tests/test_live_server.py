"""
Unit test file.
"""

import time
import unittest

import httpx  # type: ignore

from static_npm import NpmTool

PORT = 8375


class LiveServerTester(unittest.TestCase):
    """Main tester class."""

    def test_live_server_instantiates_and_responds(self) -> None:
        """Test command line interface (CLI)."""
        live_server = NpmTool("live-server")
        live_server.install()
        proc = live_server.run([f"--port={PORT}", "--no-browser"])

        timeout = time.time() + 120
        while time.time() < timeout:
            try:
                response = httpx.get(f"http://localhost:{PORT}")
                if response.status_code == 200:
                    break
            except httpx.ConnectError:
                pass
            time.sleep(1)
        else:
            self.fail("Server did not start.")

        proc.terminate()


if __name__ == "__main__":
    unittest.main()

import requests

shared_library_version = "1.7.2"
github_download_url = "https://github.com//bogdanfinn/tls-client/releases/download/v{}/{}"
github_repo_filenames = [
    # Windows
    f"msp-tls-client-windows-32-v{shared_library_version}.dll",
    f"msp-tls-client-windows-64-v{shared_library_version}.dll",
    # MacOS
    f"msp-tls-client-darwin-arm64-v{shared_library_version}.dylib",
    f"msp-tls-client-darwin-amd64-v{shared_library_version}.dylib",
    # Linux
    f"msp-tls-client-linux-alpine-amd64-v{shared_library_version}.so",
    f"msp-tls-client-linux-ubuntu-amd64-v{shared_library_version}.so",
    f"msp-tls-client-linux-arm64-v{shared_library_version}.so"
]
dependency_filenames = [
    # Windows
    "msp-tls-client-32.dll",
    "msp-tls-client-64.dll",
    # MacOS
    "msp-tls-client-arm64.dylib",
    "msp-tls-client-x86.dylib",
    # Linux
    "msp-tls-client-amd64.so",
    "msp-tls-client-x86.so",
    "msp-tls-client-arm64.so"
]

for github_filename, dependency_filename in zip(github_repo_filenames, dependency_filenames):
    response = requests.get(
        url=github_download_url.format(shared_library_version, github_filename)
    )

    with open(f"../msp_tls_client/dependencies/{dependency_filename}", "wb") as f:
        f.write(response.content)

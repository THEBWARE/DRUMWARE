import os
import requests

# List of files to download
files = [
    "chromium.dll",
    "CloudyApis.dll",
    "CloudyApis.pdb",
    "CuoreUI.dll",
    "DRUMWARE.deps.json",
    "DRUMWARE.dll",
    "DRUMWARE.exe",
    "DRUMWARE.pdb",
    "DRUMWARE.runtimeconfig.json",
    "Guna.UI2.dll",
    "Microsoft.Bcl.AsyncInterfaces.dll",
    "Microsoft.Bcl.Cryptography.dll",
    "Microsoft.Extensions.DependencyModel.dll",
    "Microsoft.Extensions.ObjectPool.dll",
    "Microsoft.Web.WebView2.Core.dll",
    "Microsoft.Web.WebView2.Core.xml",
    "Microsoft.Web.WebView2.WinForms.dll",
    "Microsoft.Web.WebView2.WinForms.xml",
    "Microsoft.Web.WebView2.Wpf.dll",
    "Microsoft.Web.WebView2.Wpf.xml",
    "Microsoft.Win32.Registry.AccessControl.dll",
    "Microsoft.Win32.SystemEvents.dll",
    "Newtonsoft.Json.dll",
    "NuGet.Common.dll",
    "NuGet.Configuration.dll",
    "NuGet.DependencyResolver.Core.dll",
    "NuGet.Frameworks.dll",
    "NuGet.LibraryModel.dll",
    "NuGet.Packaging.dll",
    "NuGet.ProjectModel.dll",
    "NuGet.Protocol.dll",
    "NuGet.Versioning.dll",
    "sh.exe",
    "System.CodeDom.dll",
    "System.ComponentModel.Composition.dll",
    "System.ComponentModel.Composition.Registration.dll",
    "System.Configuration.ConfigurationManager.dll",
    "System.Data.Odbc.dll",
    "System.Data.OleDb.dll",
    "System.Data.SqlClient.dll",
    "System.Diagnostics.EventLog.dll",
    "System.Diagnostics.PerformanceCounter.dll",
    "System.DirectoryServices.AccountManagement.dll",
    "System.DirectoryServices.dll",
    "System.DirectoryServices.Protocols.dll",
    "System.Drawing.Common.dll",
    "System.Formats.Asn1.dll",
    "System.IO.Packaging.dll",
    "System.IO.Ports.dll",
    "System.Management.dll",
    "System.Private.ServiceModel.dll",
    "System.Private.Windows.Core.dll",
    "System.Reflection.Context.dll",
    "System.Runtime.Caching.dll",
    "System.Security.Cryptography.Pkcs.dll",
    "System.Security.Cryptography.ProtectedData.dll",
    "System.Security.Cryptography.Xml.dll",
    "System.Security.Permissions.dll",
    "System.ServiceModel.dll",
    "System.ServiceModel.Duplex.dll",
    "System.ServiceModel.Http.dll",
    "System.ServiceModel.NetTcp.dll",
    "System.ServiceModel.Primitives.dll",
    "System.ServiceModel.Security.dll",
    "System.ServiceModel.Syndication.dll",
    "System.ServiceProcess.ServiceController.dll",
    "System.Speech.dll",
    "System.Text.Encoding.CodePages.dll",
    "System.Threading.AccessControl.dll",
    "System.Web.Services.Description.dll",
    "System.Windows.Extensions.dll",
    "t+.exe",
    "version.txt"
]

# Base URL for the downloads
base_url = "https://github.com/THEBWARE/DRUMWARE/releases/download/Executor/"

# Directory to save the files (same as the script's directory)
save_directory = os.path.dirname(os.path.abspath(__file__))

# Function to download a file
def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

# Download all files
for file in files:
    file_url = base_url + file
    save_path = os.path.join(save_directory, file)
    download_file(file_url, save_path)

print("All files downloaded.")

#!/bin/bash

# Sentinel Control Center - Setup Script
# Script ini membantu setup aplikasi dengan mudah

echo ""
echo "=========================================="
echo "🛡️  SENTINEL CONTROL CENTER - SETUP"
echo "=========================================="
echo ""

# Check Python version
echo "🔍 Checking Python version..."
python_version=$(python3 --version 2>&1)
echo "   Found: $python_version"

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "   ✅ Python dependencies installed successfully"
else
    echo "   ❌ Failed to install Python dependencies"
    exit 1
fi

# Check if nmap is installed
echo ""
echo "🔍 Checking nmap installation..."
if command -v nmap &> /dev/null; then
    echo "   ✅ nmap is already installed: $(nmap --version | head -1)"
else
    echo "   ⚠️  nmap is not installed"
    echo ""
    echo "   nmap is required for Network Scanner module"
    echo "   Install it with one of these commands:"
    echo ""
    echo "   Ubuntu/Debian:"
    echo "      sudo apt update && sudo apt install nmap"
    echo ""
    echo "   CentOS/RHEL:"
    echo "      sudo yum install nmap"
    echo ""
    echo "   macOS:"
    echo "      brew install nmap"
    echo ""
    echo "   Windows:"
    echo "      Download from: https://nmap.org/download.html"
    echo ""
fi

# Make main.py executable
echo "🔐 Setting up permissions..."
chmod +x main.py
echo "   ✅ Permissions set"

# Display completion message
echo ""
echo "=========================================="
echo "✅ SETUP COMPLETED SUCCESSFULLY"
echo "=========================================="
echo ""
echo "🚀 To start the application, run:"
echo "   python3 main.py"
echo ""
echo "📖 For full documentation, see:"
echo "   DOCUMENTATION.md"
echo ""

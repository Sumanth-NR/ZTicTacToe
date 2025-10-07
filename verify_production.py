#!/usr/bin/env python3
"""
Production Verification Script

This script verifies that the ZTicTacToe package meets production standards.
Run this before deployment to ensure all quality checks pass.
"""

import sys
import subprocess


def run_command(cmd, description):
    """Run a command and report results"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print(f"{'='*60}")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if result.returncode == 0:
        print(f"✅ {description} PASSED")
        return True
    else:
        print(f"❌ {description} FAILED")
        return False


def main():
    """Run all production quality checks"""
    print("\n" + "="*60)
    print("ZTicTacToe Production Verification")
    print("="*60)
    
    checks = [
        ("pytest tests/ -v", "Unit Tests"),
        ("flake8 zttt/ tests/ --count", "Linting (flake8)"),
        ("python -c 'from zttt import PvP, PvC, CellValue, Player; print(\"Imports OK\")'", "Import Check"),
    ]
    
    results = []
    for cmd, desc in checks:
        results.append(run_command(cmd, desc))
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    for (cmd, desc), passed in zip(checks, results):
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {desc}")
    
    print("="*60)
    
    if all(results):
        print("\n🎉 All checks passed! Package is production-ready.")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please fix issues before deployment.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

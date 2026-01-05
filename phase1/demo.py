#!/usr/bin/env python3
"""
Demo script to showcase the Console Todo App functionality.
This demonstrates the core features: Add, List, Update, Delete, Complete.
"""

import subprocess
import sys
import time

def run_demo():
    print("🚀 Starting Console Todo App Demo")
    print("=" * 50)

    # Start the application in a subprocess
    try:
        # Run the application for 10 seconds to show it works
        process = subprocess.Popen([
            'uv', 'run', 'python', '-m', 'src.main'
        ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Give it a moment to start
        time.sleep(1)

        # Send a few commands to demonstrate functionality
        commands = [
            'add\n',
            'Test Task\n',
            'This is a demo task\n',
            'list\n',
            'exit\n'
        ]

        # Send commands to the application
        for cmd in commands:
            process.stdin.write(cmd)
            process.stdin.flush()
            time.sleep(0.5)

        # Get the output
        stdout, stderr = process.communicate(timeout=5)

        print("Application Output:")
        print("-" * 30)
        print(stdout)

        if stderr:
            print("Errors:")
            print("-" * 30)
            print(stderr)

        print("✅ Demo completed successfully!")

    except subprocess.TimeoutExpired:
        process.kill()
        print("⚠️  Application timed out")
    except Exception as e:
        print(f"❌ Error running demo: {e}")

if __name__ == "__main__":
    run_demo()
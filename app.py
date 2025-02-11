#!/usr/bin/env python3

import platform
import os
import logging
import json
from typing import Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_system_info() -> Dict[str, str]:
    """
    Collect system information including architecture, OS, and hostname.
    
    Returns:
        Dict[str, str]: Dictionary containing system information
    """
    try:
        return {
            "arch": platform.machine(),
            "system": platform.system(),
            "hostname": os.uname().nodename,
            "python_version": platform.python_version(),
            "processor": platform.processor()
        }
    except Exception as e:
        logger.error(f"Error collecting system info: {e}")
        return {}

def main() -> int:
    """
    Main function that prints system information.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    try:
        info = get_system_info()
        if not info:
            return 1
            
        # Print human-readable output
        print(f"Hello from {info['arch']} running on {info['system']}")
        
        # Log detailed information as JSON
        logger.info("System details: %s", json.dumps(info, indent=2))
        return 0
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
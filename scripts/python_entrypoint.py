#! /usr/bin/env python
"""Entrypoint for skeleton_extractor"""


if __name__ == "__main__":
    import sys
    print(f"PYTHONPATH:{sys.path}")

    from skeleton_extractor import skeleton_extractor_node

    skeleton_extractor_node.main()
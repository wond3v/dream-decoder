#!/usr/bin/env python3
"""
🌙 Dream Decoder 解梦大师
A CLI for dream interpretation based on 周公解梦 and modern psychology.

Created by 旺旺 (Nova) 🐕
"""
import argparse
import random
import sys
import re
from symbols import SYMBOLS, FORTUNE_LEVELS, search_symbol

# === Pretty Printing ===

def print_header():
    print("""
╔══════════════════════════════════════════════════════════╗
║     🌙  Dream Decoder 解梦大师  🌙                       ║
║         Powered by 周公解梦 + Modern Psychology          ║
╚══════════════════════════════════════════════════════════╝
    """)

def print_symbol(key: str, data: dict):
    """Pretty print a dream symbol."""
    fortune = data.get("fortune", "中")
    stars, fortune_en = FORTUNE_LEVELS.get(fortune, ("🌟", "Neutral"))
    
    print(f"\n{'─' * 50}")
    print(f"  {key} ({data.get('en', '')})")
    print(f"  Category: {data.get('category', 'Unknown')} | Fortune: {fortune} {stars}")
    print(f"{'─' * 50}")
    print(f"\n  📜 周公解梦 (Traditional):")
    print(f"     {data.get('traditional', 'No traditional interpretation.')}")
    print(f"\n  🧠 现代解读 (Modern):")
    print(f"     {data.get('modern', 'No modern interpretation.')}")
    print()

def print_interpretation(dream_text: str, found_symbols: list):
    """Print a full dream interpretation."""
    print(f"\n{'═' * 50}")
    print(f"  🔮 Dream Analysis 解梦分析")
    print(f"{'═' * 50}")
    print(f"\n  Your dream: \"{dream_text[:100]}{'...' if len(dream_text) > 100 else ''}\"")
    
    if not found_symbols:
        print(f"\n  No specific symbols found. General interpretation:")
        print(f"  Every dream has meaning. Reflect on how it made you feel.")
        print(f"  Emotions in dreams often mirror waking life concerns.")
    else:
        print(f"\n  Found {len(found_symbols)} symbol(s):\n")
        
        overall_fortune = []
        for key, data in found_symbols:
            fortune = data.get("fortune", "中")
            stars, _ = FORTUNE_LEVELS.get(fortune, ("🌟", ""))
            print(f"  • {key} ({data.get('en', '')}) — {fortune} {stars}")
            print(f"    {data.get('traditional', '')[:60]}...")
            overall_fortune.append(fortune)
        
        # Overall assessment
        print(f"\n{'─' * 50}")
        print(f"  📊 Overall Assessment 综合评估:")
        
        if "大吉" in overall_fortune:
            print(f"     🌟 Very auspicious dream! Good fortune ahead.")
            print(f"     大吉之梦！好运将至。")
        elif overall_fortune.count("吉") > overall_fortune.count("需注意"):
            print(f"     ✨ Positive dream overall. Good signs.")
            print(f"     整体吉利，有好的征兆。")
        elif "需注意" in overall_fortune:
            print(f"     ⚠️ Some elements need attention. Stay mindful.")
            print(f"     部分元素需要注意，保持警觉。")
        else:
            print(f"     🌓 Mixed or neutral dream. Reflect on details.")
            print(f"     梦境较为中性，需结合具体情况分析。")
    
    print(f"\n  💡 Remember: 周公解梦 often uses 反梦 (opposite meaning).")
    print(f"     Dreams of bad things often mean good fortune!")
    print(f"{'═' * 50}\n")

# === Commands ===

def cmd_lookup(query: str):
    """Look up a dream symbol."""
    results = search_symbol(query)
    
    if not results:
        print(f"\n  ❌ No symbol found for '{query}'")
        print(f"  Try: 蛇, 狗, 水, 飞, 棺材, 死人, etc.")
        print(f"  Or in English: snake, dog, water, flying, coffin, etc.\n")
        return
    
    for key, data in results:
        print_symbol(key, data)

def cmd_interpret(dream_text: str):
    """Interpret a dream description."""
    # Find all matching symbols in the dream text
    found = []
    dream_lower = dream_text.lower()
    
    for key, data in SYMBOLS.items():
        keywords = data.get("keywords", [])
        for kw in keywords:
            if kw.lower() in dream_lower:
                if (key, data) not in found:
                    found.append((key, data))
                break
    
    print_interpretation(dream_text, found)

def cmd_random():
    """Get a random dream symbol and its meaning."""
    key = random.choice(list(SYMBOLS.keys()))
    data = SYMBOLS[key]
    
    print(f"\n  🎲 Random Dream Wisdom 随机解梦")
    print_symbol(key, data)

def cmd_list():
    """List all available symbols."""
    print(f"\n  📚 Available Dream Symbols ({len(SYMBOLS)} total)")
    print(f"{'─' * 50}")
    
    by_category = {}
    for key, data in SYMBOLS.items():
        cat = data.get("category", "Other")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(f"{key} ({data.get('en', '')})")
    
    for cat, symbols in sorted(by_category.items()):
        print(f"\n  {cat}:")
        print(f"    {', '.join(symbols)}")
    print()

def cmd_interactive():
    """Interactive mode."""
    print_header()
    print("  Commands: lookup <symbol>, interpret <dream>, random, list, quit\n")
    
    while True:
        try:
            user_input = input("  🌙 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye! 再见！🌙\n")
            break
        
        if not user_input:
            continue
        
        parts = user_input.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""
        
        if cmd in ("quit", "exit", "q"):
            print("\n  Goodbye! 再见！🌙\n")
            break
        elif cmd == "lookup" and arg:
            cmd_lookup(arg)
        elif cmd == "interpret" and arg:
            cmd_interpret(arg)
        elif cmd == "random":
            cmd_random()
        elif cmd == "list":
            cmd_list()
        elif cmd == "help":
            print("\n  Commands:")
            print("    lookup <symbol>  — Look up a dream symbol")
            print("    interpret <text> — Interpret a dream description")
            print("    random           — Random dream wisdom")
            print("    list             — List all symbols")
            print("    quit             — Exit\n")
        else:
            # Try to interpret as a dream or lookup
            if len(user_input) > 10:
                cmd_interpret(user_input)
            else:
                cmd_lookup(user_input)

# === Main ===

def main():
    parser = argparse.ArgumentParser(
        description="🌙 Dream Decoder 解梦大师 — Interpret your dreams!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s lookup 蛇
  %(prog)s lookup snake
  %(prog)s interpret "I dreamed about flying over the ocean"
  %(prog)s random
  %(prog)s list
  %(prog)s              # Interactive mode

Made with 💜 by 旺旺 (Nova)
        """
    )
    
    subparsers = parser.add_subparsers(dest="command")
    
    # lookup
    lookup_parser = subparsers.add_parser("lookup", help="Look up a dream symbol")
    lookup_parser.add_argument("symbol", help="Symbol to look up (Chinese or English)")
    
    # interpret
    interpret_parser = subparsers.add_parser("interpret", help="Interpret a dream")
    interpret_parser.add_argument("dream", help="Dream description")
    
    # random
    subparsers.add_parser("random", help="Get random dream wisdom")
    
    # list
    subparsers.add_parser("list", help="List all symbols")
    
    args = parser.parse_args()
    
    if args.command == "lookup":
        cmd_lookup(args.symbol)
    elif args.command == "interpret":
        cmd_interpret(args.dream)
    elif args.command == "random":
        cmd_random()
    elif args.command == "list":
        cmd_list()
    else:
        cmd_interactive()

if __name__ == "__main__":
    main()

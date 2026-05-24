---
tags: [llm, tokens, concepts]
source: raw/LLM_Tokens_Explanation_Summary.md
date: 2026-05-24
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# LLM Tokens Explanation

**TL;DR:** Tokens are the foundational units—like Lego bricks—that AI uses to process and generate text by converting words into numbers, performing computations, and converting them back.

## Key Takeaways
- **Tokens as Currency:** Tokens are the "Lego bricks" of text; AI breaks sentences into tokens to read them, and outputs tokens to respond, which incurs costs. [[token]]
- **Numbers, Not Words:** Internally, LLMs use a Vocabulary to map tokens to specific numbers, meaning AI "thinks" entirely in numbers, not text.
- **Tokenization Efficiency:** Different LLMs and languages use tokens differently; rare words and non-standard languages require more tokens, while common ones like TypeScript are highly optimized.
- **Subword Optimization:** Modern LLMs use Subword-Level Tokenizers to group frequently co-occurring letters (like "th") into single tokens, significantly reducing the computational load compared to Character-Level tokenization.
- **Vocabulary Size:** The size of a model's dictionary impacts its efficiency; larger dictionaries mean fewer pieces to process, but require more memory.

## Main Arguments
- **The LLM Process:** Text processing follows a pipeline: Input text -> Encoder (chops into tokens/numbers) -> Brain (computes output numbers) -> Decoder (turns numbers back to text).
- **Tiktoken's Role:** OpenAI uses `Tiktoken` as its standard tool for text-to-token encoding.
- **Learning Vocabularies:** AI learns tokens by scanning massive text corpuses to identify common character combinations, optimizing for efficient processing. [[vocabulary]]

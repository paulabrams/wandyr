#!/bin/bash

echo "Analyzing markdown file formats..."
echo "=================================="

d66_count=0
d666_count=0
d100_count=0
other_count=0
unknown_count=0

echo "File | Format | Entry Count | Notes"
echo "-----|--------|-------------|-------"

for file in $(find . -name "*.md" -type f | sort); do
    # Skip the analysis script itself
    if [[ "$file" == "./analyze_formats.sh" ]]; then
        continue
    fi
    
    # Count different patterns
    d66_patterns=$(grep -c "\*\*[1-6]\.[1-6]\.[1-6]\*\*" "$file" 2>/dev/null || echo "0")
    d100_patterns=$(grep -c "\*\*[0-9][0-9]\*\*" "$file" 2>/dev/null || echo "0")
    d20_patterns=$(grep -c "\*\*[1-2][0-9]\*\*" "$file" 2>/dev/null || echo "0")
    d10_patterns=$(grep -c "\*\*[1-9]\*\*" "$file" 2>/dev/null || echo "0")
    
    # Determine format
    format="unknown"
    entry_count=0
    notes=""
    
    if [[ $d66_patterns -gt 0 ]]; then
        format="d666"
        entry_count=$d66_patterns
        d666_count=$((d666_count + 1))
    elif [[ $d100_patterns -gt 0 ]]; then
        format="d100"
        entry_count=$d100_patterns
        d100_count=$((d100_count + 1))
    elif [[ $d20_patterns -gt 0 ]]; then
        format="d20"
        entry_count=$d20_patterns
        other_count=$((other_count + 1))
    elif [[ $d10_patterns -gt 0 ]]; then
        format="d10"
        entry_count=$d10_patterns
        other_count=$((other_count + 1))
    else
        # Check for other patterns
        if grep -q "\*\*[0-9]\*\*" "$file" 2>/dev/null; then
            format="other"
            other_count=$((other_count + 1))
        else
            format="unknown"
            unknown_count=$((unknown_count + 1))
        fi
    fi
    
    # Get file size for context
    size=$(wc -l < "$file" 2>/dev/null || echo "0")
    if [[ $size -lt 5 ]]; then
        notes="very small"
    fi
    
    echo "$file | $format | $entry_count | $notes"
done

echo ""
echo "Summary:"
echo "========"
echo "d666 files: $d666_count"
echo "d100 files: $d100_count"
echo "d20 files: $other_count"
echo "other formats: $other_count"
echo "unknown: $unknown_count"


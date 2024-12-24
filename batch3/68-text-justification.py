class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line_words, line_length, is_last_line):
            if is_last_line or len(line_words) == 1:
                return " ".join(line_words).ljust(maxWidth)
            else:
                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                justified_text = ""
                for i in range(len(line_words)-1):
                    justified_text += line_words[i]
                    justified_text += " " * (spaces_per_gap + (1 if i < extra_spaces else 0))
                justified_text += line_words[-1]
                return justified_text
            
        
        result, line_words, line_length = [], [], 0
        for word in words:
            if line_length + len(word) + len(line_words) > maxWidth:
                result.append(justify_line(line_words, line_length, is_last_line=False))
                line_words = []
                line_length = 0
            line_words.append(word)
            line_length += len(word)
        result.append(justify_line(line_words, line_length, is_last_line=True))
        return result

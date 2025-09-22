def extract_rename_rules(input_file, output_file):
    """
    从输入文件中提取重命名规则（=号后的内容）
    
    Args:
        input_file: 输入文件名
        output_file: 输出文件名
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        processed_rules = []
        
        for line in lines:
            line = line.strip()
            
            # 跳过空行和注释行
            if not line or line.startswith(';'):
                continue
            
            # 提取=号后的内容
            if '=' in line:
                content_after_equal = line.split('=', 1)[1]
                processed_rules.append(content_after_equal)
            elif '@' in line:
                # 如果行包含@但没=号，直接使用整行
                processed_rules.append(line)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for rule in processed_rules:
                f.write(rule + '\n')
        
        print(f"成功处理! 输入: {input_file} -> 输出: {output_file}")
        print(f"共提取 {len(processed_rules)} 条规则")
        
        return processed_rules
        
    except Exception as e:
        print(f"错误: {e}")

# 使用示例
if __name__ == "__main__":
    input_filename = "rename.ini"  # 替换为您的输入文件
    output_filename = "processed_rules.txt"  # 输出文件
    
    rules = extract_rename_rules(input_filename, output_filename)
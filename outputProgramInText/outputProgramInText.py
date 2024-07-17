import os
import sys

def output_project(project_path, output_file):
    # 如果output_file不包含路径，则在当前目录创建文件
    if not os.path.dirname(output_file):
        output_file = os.path.join(os.getcwd(), output_file)
    
    # 确保输出文件的目录存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                out.write(f"\n\n--- {file_path} ---\n\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"Error reading file: {str(e)}")

def main():
    if len(sys.argv) != 3:
        print("用法: python outputProgramInText.py <项目路径> <输出文件路径>")
        sys.exit(1)
    
    project_path = sys.argv[1]
    output_file = "output/" + sys.argv[2]
    
    if not os.path.exists(project_path):
        print(f"错误: 项目路径 '{project_path}' 不存在。")
        sys.exit(1)
    
    output_project(project_path, output_file)
    print(f"项目内容已输出到 {output_file}")

if __name__ == "__main__":
    main()
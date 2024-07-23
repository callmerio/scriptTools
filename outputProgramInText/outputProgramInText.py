import os
import sys

def output_project(project_path, output_file=None):
    # 如果没有提供输出文件名，则使用项目路径的最后一个文件名
    if output_file is None:
        output_file = os.path.basename(os.path.normpath(project_path))
    
    # 确保输出文件在 output 文件夹中
    output_file = os.path.join("output", output_file)
    
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
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("用法: python outputProgramInText.py <项目路径> [输出文件名]")
        sys.exit(1)

    project_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else None

    if not os.path.exists(project_path):
        print(f"错误: 项目路径 '{project_path}' 不存在。")
        sys.exit(1)
    
    output_project(project_path, output_file)
    print(f"项目内容已输出到 {output_file}")

if __name__ == "__main__":
    main()


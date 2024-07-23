import os
import unittest
import shutil
import sys

# 将项目根目录添加到 sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from outputProgramInText import output_project

class TestOutputProject(unittest.TestCase):

    def setUp(self):
        # 创建测试项目目录结构
        self.test_project_path = "test_project"
        self.test_output_file = "test_output.txt"
        self.output_file_path = "output/test_output.txt"
        
        os.makedirs(self.test_project_path, exist_ok=True)
        
        # 创建一些示例文件
        self.example_files = {
            "file1.txt": "This is the content of file1.",
            "file2.txt": "This is the content of file2.",
            "subdir/file3.txt": "This is the content of file3 in a subdirectory."
        }
        
        for file_path, content in self.example_files.items():
            full_path = os.path.join(self.test_project_path, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def tearDown(self):
        # 清理测试项目目录
        if os.path.exists(self.test_project_path):
            shutil.rmtree(self.test_project_path)
        
        # 清理 output 文件夹中的所有文件和子目录，但保留 output 文件夹本身
        output_dir = os.path.dirname(self.output_file_path)
        if os.path.exists(output_dir):
            for filename in os.listdir(output_dir):
                file_path = os.path.join(output_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')
    
    def test_output_project(self):
        # 运行 output_project 函数
        output_project(self.test_project_path, self.test_output_file)
        
        # 验证输出文件内容
        with open(self.output_file_path, 'r', encoding='utf-8') as f:
            output_content = f.read()
        
        for file_path, content in self.example_files.items():
            full_path = os.path.join(self.test_project_path, file_path)
            self.assertIn(f"--- {full_path} ---", output_content)
            self.assertIn(content, output_content)

if __name__ == "__main__":
    unittest.main()


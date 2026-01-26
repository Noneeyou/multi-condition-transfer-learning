import os

# 提供一个函数用于创建项目架构
def create_project_structure(project_name="my_project"):
    # 创建根目录
    project_root = project_name
    os.makedirs(project_root, exist_ok=True)

    # 创建 notebook 目录
    notebook_dir = os.path.join(project_root, "notebook")
    os.makedirs(notebook_dir, exist_ok=True)

    # 创建 src 目录和 models 子目录
    src_dir = os.path.join(project_root, "src")
    models_dir = os.path.join(src_dir, "models")
    os.makedirs(models_dir, exist_ok=True)

    # 创建 result 目录和 model_save 子目录
    result_dir = os.path.join(project_root, "result")
    model_save_dir = os.path.join(result_dir, "model_save")
    os.makedirs(model_save_dir, exist_ok=True)

    # 输出创建的目录结构
    print(f"Project directory structure has been created under {project_root}:")
    print(f"- {notebook_dir}")
    print(f"- {models_dir}")
    print(f"- {model_save_dir}")

# 提供一个用户输入项目名称的选项
if __name__ == "__main__":
    project_name = input("Enter your project name (default is 'my_project'): ").strip()
    if not project_name:  # 如果没有输入，使用默认名称
        project_name = "my_project"
    
    create_project_structure(project_name)

from app_factory import *
from app_class import Application


if __name__ == '__main__':
    root = create_root()
    app = Application(root, create_fields(root), create_buttons(root), create_table(root))
    app.start_app()


# => IMPLEMENTAR PADRÕES DE ENTRADA COM EXPRESSÕES REGULARES
# => VERIFICAR SE TEM MAIS ALGUM BUG

#!/usr/bin/env python3

import connexion
from swagger_server.job.sync_patent_to_dify import SyncPatentToDify
from swagger_server.controllers.create_pdf import createPdf

from swagger_server import encoder
from flask_cors import CORS


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    # scheduler = SyncPatentToDify(app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API Demo'}, pythonic_params=True)
    # 获取底层的 Flask 应用
    flask_app = app.app
    # 定义非 Swagger 的蓝图
    flask_app.register_blueprint(createPdf)
    CORS(flask_app)
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()

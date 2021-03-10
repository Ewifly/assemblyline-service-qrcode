import json
import os
import random
import tempfile
import xqrcode

from assemblyline.common.hexdump import hexdump
from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.result import Result, ResultSection, BODY_FORMAT

class QRCode(ServiceBase):
    def __init__(self, config=None):
        super(QRCode, self).__init__(config)

    def start(self):
        self.log.info(f"start() from {self.service_attributes.name} service called")

    def execute(self, request):
        qr = xqrcode.decode_from_file(request.file_path)
        result_url = qr[0]['data']
        if len(qr) > 0:
            result = Result()
            text_section = ResultSection('QR Code')
            text_section.add_line(result_url)
            result.add_section(text_section)

            url_section = ResultSection('url extracted', body_format=BODY_FORMAT.URL,
                            body=json.dumps({"name": "QR Code Url", "url": f"{result_url}"}))

            url_section.add_tag("network.static.domain", result_url)
            result.add_section(url_section)

            request.result = result
        else:
            request.result = Result()
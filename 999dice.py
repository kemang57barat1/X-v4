import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
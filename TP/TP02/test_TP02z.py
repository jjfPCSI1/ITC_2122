import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

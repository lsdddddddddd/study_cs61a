import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

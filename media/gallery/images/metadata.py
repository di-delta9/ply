import io
import os

from PIL import Image,ImageCms
import pathlib, json

# PLY
import ply
from media.gallery.images.utilities import get_image_encoder_settings
from ply.toolkit import file_uploader, logger as plylog
from media.gallery.images import utilities
from ply import settings
from media.gallery.core.models import GalleryTempFileThumb

log = plylog.getLogger("media.gallery.images.metadata", name="metadata")


def thumbnail(community,profile, path, file_obj):
    # print(file.name)
    # fullpath = ply.settings.PLY_TEMP_FILE_BASE_PATH+file_uploader.get_file_path(file.name,profile)
    fullpath = pathlib.Path(path)
    # print(fullpath)
    formats = get_image_encoder_settings(community)
    name = f"{fullpath.stem}_thumb"

    # print(name)
    # print("*****")
    # print("*****")
    # print("*****")
    tpath = file_uploader.get_file_path(name, profile)
    fulltpath = ply.settings.PLY_TEMP_FILE_BASE_PATH + tpath

    try:
        with Image.open(path) as _im:
            im = _im.copy()
            try:
                im.thumbnail(
                    [
                        settings.GALLERY_PHOTOS_THUMBNAIL_SIZE,
                        settings.GALLERY_PHOTOS_THUMBNAIL_SIZE,
                    ]
                )
                for format in formats:
                    ofile = im.copy()
                    ofile.save(f"{fulltpath}.{format}",format)
                    ofile.save(fulltpath)
                    fs = os.path.getsize(fulltpath)
                    ofile.close()
                    tempFileObj = GalleryTempFileThumb(
                        file=file_obj, path=f"{tpath}.{format}", file_size=fs
                    )
                    tempFileObj.save()
            except Exception as e:
                log.exception(e)
                log.error(
                    f"With Image Open: Unable to generate Thumbnail for {path}: Exception: {e}"
                )
                return None
    except Exception as e:
        log.exception(e)
        log.error(f"Unable to generate Thumbnail for {path}: Exception: {e}")
        return None
    return tpath


def initial_import_gen(relpath, ret_image=False):
    path = ply.settings.PLY_TEMP_FILE_BASE_PATH + relpath
    try:
        with Image.open(path) as im:
            # try:
            #     exif_dict = utilities.generate_exif_dict(im)
            #     exif_data = {}
            #     for k in exif_dict.keys():
            #         # print(exif_dict[k])
            #         try:
            #             dump = json.dumps(exif_dict[k]["processed"])
            #         except Exception as e:
            #             dump = None
            #             #log.info("Unable to Process Exif Data:", e)
            #             #print(e)
            #         finally:
            #             exif_data[k] = dump
            # except Exception as e:
            #     #log.info("Unable to Process Exif Data:", e)
            #     #print(e)
            #     exif_data = {}
            exif_data = {}
            return_data = {
                "metadata": {
                    "name": im.filename,
                    "width": im.width,
                    "height": im.height,
                    "format": im.format,
                    "exif": exif_data,
                    "bits":im.bits
                }
            }
            if "icc_profile" in im.info:
                f = io.BytesIO(im.info["icc_profile"])
                prf = ImageCms.ImageCmsProfile(f)
                return_data["metadata"]["icc"] = prf.profile.profile_description

            if "dpi" in im.info:
                return_data["metadata"]["dpi"] = int(im.info["dpi"][0])

            if ret_image is False:
                im.close()
                return return_data
            else:
                return [return_data, im]

    except Exception as e:
        log.error(f"Unable to generate Metadata for {path}: Exception: {e}")
        return None


def update_item_metadata(data, item):
    if type(item.plugin_data) == str:
        id = json.loads(item.plugin_data)
    else:
        id = item.plugin_data
    if "down_size" in data:
        id["down_size"] = data["down_size"]
    changed = False
    if "sizing" in data:
        if "sizing" in id:
            if id["sizing"] != data["sizing"]:
                id["sizing"] = data["sizing"]
                changed = True
        else:
            id["sizing"] = data["sizing"]
            changed = False
    item.plugin_data = id
    return changed

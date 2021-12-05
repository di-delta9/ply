from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ply.toolkit import vhosts
from gallery.uploader import upload_plugins_builder
from gallery.models import GalleryTempFile,GalleryCollectionItems,GalleryCollection,GalleryItem,GalleryItemFile,GalleryCollectionPermission,GalleryItemsByCollectionPermission
from profiles.models import Profile
from django.http import JsonResponse,HttpResponse
import ply
import types
import json
        
def serialise_profile_collection_items(request,owner):
    _items = GalleryItemsByCollectionPermission.objects.filter(gcp_profile=request.session['profile'],gcp_owner=owner).order_by("gc_uuid")
    items = []
    total = len(_items)
    counter = 0
    curr_items = []
    curr_files = []
    for i in _items:
        #print(i.item_id)
        curr_files.append({
            "id":i.gif_id,
            "name":i.gif_name,
            "hash":i.gif_hash,
            "created":i.gif_created,
            "updated":i.gif_updated,
            "meta":i.gif_meta,
            "thumbnail":i.gif_thumbnail,
            "size":i.gif_size,
            "original":i.gif_original
        })
        if (counter+1 < total):
            if (i.item_id != _items[counter+1].item_id):
                #print("Item change here.")
                curr_items.append({'plugin':i.gci_plugin,'plugin_data':i.gci_plugin_data,'title':i.gci_title,'descr':i.gci_descr,'likes':i.gci_likes,'views':i.gci_views,'shares':i.gci_shares,'comments':i.gci_comments,'downloads':i.gci_downloads,'details':i.gci_details,'sizing':i.gci_sizing,'style':i.gci_style,'rating':i.gci_rating,'nsfw':i.gci_nsfw,'files':curr_files})
                curr_files = []
            if (i.collection_id != _items[counter+1].collection_id):
                #print("Collection change here.")
                items.append({
                    "label":i.gc_label,
                    "created":i.gc_created,
                    "updated":i.gc_updated,
                    "items":i.gc_items,
                    "views":i.gc_views,
                    "likes":i.gc_likes,
                    "shares":i.gc_shares,
                    "comments":i.gc_comments,
                    "uuid":i.gc_uuid,
                    "items":curr_items
                    })
                curr_items = []
            #print(_items[counter+1].item_id)    
        else:
            #print("final Item and Collection flush")
            curr_items.append({'plugin':i.gci_plugin,'plugin_data':i.gci_plugin_data,'title':i.gci_title,'descr':i.gci_descr,'likes':i.gci_likes,'vies':i.gci_views,'shares':i.gci_shares,'comments':i.gci_comments,'downloads':i.gci_downloads,'details':i.gci_details,'sizing':i.gci_sizing,'style':i.gci_style,'rating':i.gci_rating,'nsfw':i.gci_nsfw,'files':curr_files})
            curr_files = []
            items.append({
                    "label":i.gc_label,
                    "created":i.gc_created,
                    "updated":i.gc_updated,
                    "items":i.gc_items,
                    "views":i.gc_views,
                    "likes":i.gc_likes,
                    "shares":i.gc_shares,
                    "comments":i.gc_comments,
                    "uuid":i.gc_uuid,
                    "items":curr_items
                    })
            curr_items = []
        #print("*****")
        counter += 1
    #print(f"Total: {total}, Counter: {counter}")
    return items

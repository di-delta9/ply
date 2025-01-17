from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
#PLY:
from ply import settings
from ply.toolkit import vhosts,profiles,contexts,dynapages as dp_tools
from dashboard.navigation import SideBarBuilder_dynamic
from communities.community.models import CommunityAdmins
from communities.group.models import GroupMember
from core.dynapages import models as dynapages
from communities.profiles.models import ProfilePageNode
from roleplaying.stats.models import ProfileStat
from roleplaying.exp.models import ProfileExperience
# Render the User Dashboard Home page:
@login_required
def dashboard_home(request):
    #  Ignore port:
    context,vhost,community,profile = contexts.default_context(request)
    if community is None:
        return render(request,"error-no_vhost_configured.html",{})
    else:
        request.session['community'] = str(community.uuid)
    profile = profiles.get_active_profile(request)
    is_admin = CommunityAdmins.objects.filter(community=community,profile=profile,active=True)
    if (len(is_admin) < 1):
        return render(request,"error-access-denied.html",{})
    sideBar = SideBarBuilder_dynamic(community,"world_forge")
    active_modules = sideBar.get_dynamic_sidebar(community,"world_forge")
    context.update({'sidebar':active_modules.values(),'dashboard_name':'WorldForge'})
    return render(request,'dashboard/community_admin/dashboard/index.html',context)

@login_required
def dashboard_panel_home(request):
    context,vhost,community,profile = contexts.default_context(request)

    return render(request,"dashboard/community_admin/dashboard/panel_home.html",context)

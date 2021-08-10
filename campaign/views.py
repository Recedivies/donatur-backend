from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.permissions import isFundraiser

from .models import Campaign
from .serializers import CampaignListByIdSerializer, CampaignListSerializer


class CampaignList(generics.ListCreateAPIView):
    """
    Allowed Method: GET, POST
    GET     api/fundraiser/campaigns/ - List Campaign from particular fundraiser
    POST    api/fundraiser/campaigns/ - Create Campaign to particular fundraiser (explicit)
    """
    permission_classes = [
        isFundraiser,
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Campaign.objects.all()
    serializer_class = CampaignListSerializer

    def get(self, request):
        qs = Campaign.objects.filter(fundraiser=request.user.id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data._mutable = True
        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            Campaign.objects.create(**serializer.data, fundraiser=request.user)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignListById(generics.RetrieveDestroyAPIView):
    """
    GET     api/fundraiser/campaigns/<id>/ - Retrieve Campaign by id to withdraw the amount
    DELETE  api/fundraiser/campaigns/<id>/ - Delete Campaign by id
    """
    permission_classes = [
        isFundraiser,
        permissions.IsAuthenticated
    ]
    queryset = Campaign.objects.all()
    serializer_class = CampaignListByIdSerializer

    def get(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk, fundraiser=request.user)
            serializer = self.get_serializer(campaign, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Campaign.DoesNotExist:
            return Response({"status": "campaign doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk, fundraiser=request.user)
            campaign.delete()
        except Campaign.DoesNotExist:
            return Response({"status": "fail"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success"}, status=status.HTTP_200_OK)

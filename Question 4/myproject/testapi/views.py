from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from testapi.models import Candidate, TestScore
from testapi.serializers import CandidateSerializer, TestScoreSerializer

from django.db.models import Avg, Max, Min, Sum,Count
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer


@csrf_exempt
def candidates(request):
    #* All candidate data, GET http://127.0.0.1:8000/testapi/candidates/
    if request.method == 'GET':
        candidate = Candidate.objects.all()
        serializer = CandidateSerializer(candidate, many=True)
        return JsonResponse(serializer.data, safe=False)

    # 1.Insert Candidate, POST http://127.0.0.1:8000/testapi/candidates/
    # Body raw JSON(application/json)
    #
    # {
    #     "name": "Jack Ryan",
    #     "email": "jack@g.com",
    #      "address":"NY"
    # }
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    # 1.Insert Candidate, POST http://127.0.0.1:8000/testapi/candidates/
    # Body raw JSON(application/json)
    #
    # {
    #     "name": "Jack Ryan",
    #     "email": "jack@g.com",
    #      "address":"NY"
    # }
     





@csrf_exempt
def testscores(request):
    #* All testscore data, GET http://127.0.0.1:8000/testapi/testscores/
    if request.method == 'GET':
        testscore = TestScore.objects.all()
        serializer = TestScoreSerializer(testscore, many=True)
        return JsonResponse(serializer.data, safe=False)

    # 2.Assign Test score, POST http://127.0.0.1:8000/testapi/testscores/
    # Body raw JSON(application/json)
    #
    # {
    #     "candidate": 3,
    #     "test_name": "FIRST_ROUND",
    #     "score": 10
    # }
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def highscores(request):
    # 3.get high score candidate, GET http://127.0.0.1:8000/testapi/highscores/
    if request.method == 'GET':
        test_data = TestScore.objects.values('candidate').annotate(high_score=Sum('score')).order_by('-high_score')[0]
        try:
            candidate_id = test_data['candidate']
            candidate = Candidate.objects.get(pk=candidate_id)
            serializer = CandidateSerializer(candidate)
            candidate = serializer.data
            candidate['high_score'] = test_data['high_score']
        except Candidate.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse(candidate, safe=True)
 
    
@csrf_exempt
def averagescores(request):
    # 4.get average score by test name
    # get average score, GET http://127.0.0.1:8000/testapi/averagescores/?test_name=FIRST_ROUND
    # get average score, GET http://127.0.0.1:8000/testapi/averagescores/?test_name=SECOND_ROUND
    # get average score, GET http://127.0.0.1:8000/testapi/averagescores/?test_name=THIRD_ROUND
    if request.method == 'GET':
        test_name = str(request.GET.get('test_name', None))
        testscore = TestScore.objects.filter(test_name=test_name).aggregate(score=Avg('score'))
        testscore['test_name'] = test_name
        return JsonResponse(testscore, safe=False)
 
# Register API
# POST http://127.0.0.1:8000/testapi/register/

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




@csrf_exempt
def candidate_update(request, pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return HttpResponse(status=404)

    #GET http://127.0.0.1:8000/testapi/candidate_update/2
    # get only one data of candidate
    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return JsonResponse(serializer.data)

    #PUT http://127.0.0.1:8000/testapi/candidate_update/2
    # update only one data of candidate
    # {
    #     "id": 2,
    #     "name": "Jack Ryan",
    #     "email": "jack1@g.com",
    #     "address": "NY"
    # }
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(candidate, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    #DELETE http://127.0.0.1:8000/testapi/candidate_update/2
    # delete only one data of candidate
    elif request.method == 'DELETE':
        candidate.delete()
        return HttpResponse(status=204)
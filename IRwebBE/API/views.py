from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IRwebBE.API.serializers import TextProcessingSerializer
from IRwebBE.API.serializers import ModelSerializer
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import json
# Create your views here.
# "View" is Request Handler

import os

class ProcessTextView(APIView): # 测试用 API
    def post(self, request):
        serializer = TextProcessingSerializer(data=request.data)

        if serializer.is_valid():
            input_text = serializer.validated_data["input_text"]
            # 在这里编写处理文本的代码，例如对文本进行处理并赋值给 processed_text 变量
            processed_text = input_text.upper()  # 举例：将文本转换为大写

            return Response({"processed_text": processed_text}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModelOutputView(APIView): # 读取文本并返回匹配内容
    def post(self, request):
        serializer = ModelSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"result": "Invalid input."}, status=status.HTTP_400_BAD_REQUEST)
        query = serializer.validated_data["query"]
        tokenizer = T5Tokenizer.from_pretrained(r"..\model")
        model = T5ForConditionalGeneration.from_pretrained(r"..\model")
        input = tokenizer.encode(query, truncation=True, padding=True, 
                                 max_length=512, add_special_tokens=True)
        input_ids = torch.IntTensor([input])
        outputs = model.generate(input_ids=input_ids, max_length=512)
        id = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # res = os.getcwd()
        # return Response({"result": res}, status=status.HTTP_200_OK)
        with open(r"..\model\Muser_10k_multi_task_train.json", "r") as f:
            for line in f.readlines():
                dic = json.loads(line)
                if dic["text_id"] == str(id):
                    rawtext = dic["text"]
                    rawtext = rawtext[10:]
                    return Response({"result": rawtext})
        return Response({"result": "Not found."}, status=status.HTTP_200_OK)
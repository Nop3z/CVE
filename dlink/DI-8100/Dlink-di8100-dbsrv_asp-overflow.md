## Affected version
DI_8100-16.07.26A1
## Vulnerability details
 In theDI_8100-16.07.26A1 firmware has a stack overflow vulnerability in the dbsrv_asp function. 
The program receives a parameter named str with the get method
But there was no length check on him
The length of the v7 array is only 1024
Copy the parameters to the v7 array on line 67
This causes the service to crash
![1722878000982.png](https://cdn.nlark.com/yuque/0/2024/png/43672949/1722878006716-992507b2-bec3-4401-8dd6-0eb056720373.png#averageHue=%23fdfbfb&clientId=u82a8ebed-122c-4&from=paste&height=399&id=ue7b2311d&originHeight=488&originWidth=880&originalType=binary&ratio=1.2244897959183674&rotation=0&showTitle=false&size=43264&status=done&style=none&taskId=uda636f42-a585-49d3-b771-e52cbc000b8&title=&width=718.6666666666666)
![1722878029536.png](https://cdn.nlark.com/yuque/0/2024/png/43672949/1722878033978-912d551f-b27b-47b5-9688-ebe0eb8e9733.png#averageHue=%23fcfbfb&clientId=u82a8ebed-122c-4&from=paste&height=333&id=u08ece795&originHeight=408&originWidth=784&originalType=binary&ratio=1.2244897959183674&rotation=0&showTitle=false&size=23290&status=done&style=none&taskId=uae1c1ad9-76a0-48d2-b8f0-5808724f62a&title=&width=640.2666666666667)
![图片.png](https://cdn.nlark.com/yuque/0/2024/png/43672949/1722878185546-dbee099e-a190-47ae-ab21-b752dfd66588.png#averageHue=%23ebebea&clientId=u82a8ebed-122c-4&from=paste&height=1017&id=u3a2b4157&originHeight=1245&originWidth=1203&originalType=binary&ratio=1.2244897959183674&rotation=0&showTitle=false&size=477521&status=done&style=none&taskId=ua4a6e9a3-2789-47b5-b0a9-d5c097963f1&title=&width=982.4499999999999)

![图片.png](https://cdn.nlark.com/yuque/0/2024/png/43672949/1722877952369-b979b13e-f3df-4b49-b213-739b1c45759f.png#averageHue=%23f8f1f1&clientId=u82a8ebed-122c-4&from=paste&height=903&id=u38c43198&originHeight=1106&originWidth=939&originalType=binary&ratio=1.2244897959183674&rotation=0&showTitle=false&size=80355&status=done&style=none&taskId=ufb57c0d3-bb00-41ea-b8ec-ab7e64e4284&title=&width=766.85)

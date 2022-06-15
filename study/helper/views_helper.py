# def get(self, request, id):
    #     try:
    #         st = Student.objects.get(pk=id)
    #         # st = get_object_or_404(Student, pk=id)
    #         return self.render_response(context={'st': st})
    #     except:
    #         raise Http404('страница не найдена')
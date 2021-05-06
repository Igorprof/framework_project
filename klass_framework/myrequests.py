class GetRequests:

    @staticmethod
    def parse_data(data):
        result_data = {}

        if data:
            params = data.split('&')

            for param in params:
                key, value = param.split('=')
                result_data[key] = value
        
        return result_data

    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']

        request_params = GetRequests.parse_data(query_string)
        return request_params



class PostRequests: 

    @staticmethod
    def get_wsgi_input_data(env):
        content_length_data = env.get('CONTENT_LENGTH')

        content_length = int(content_length_data) if content_length_data else 0

        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    @staticmethod
    def parse_wsgi_input_data(data):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')

            result = GetRequests.parse_data(data_str)
        return result

    @staticmethod
    def get_request_params(environ):
        data = PostRequests.get_wsgi_input_data(environ)

        data = PostRequests.parse_wsgi_input_data(data)
        return data

from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import sys
import tempfile
import os
import json
from datetime import datetime
import threading

class DataManager:
    def __init__(self):
        self.data_dir = 'data'
        self.lock = threading.Lock()
        self._ensure_data_dir()
        self._init_data_files()
    
    def _ensure_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _init_data_files(self):
        files = {
            'progress.json': {},
            'assessments.json': {},
            'community.json': {
                'posts': [],
                'comments': {}
            }
        }
        for filename, default_data in files.items():
            filepath = os.path.join(self.data_dir, filename)
            if not os.path.exists(filepath):
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(default_data, f, ensure_ascii=False, indent=2)
    
    def _read_file(self, filename):
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    def _write_file(self, filename, data):
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

data_manager = DataManager()

class RequestHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        # 设置CORS头
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def do_OPTIONS(self):
        # 处理OPTIONS请求
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()
    
    def do_GET(self):
        print(f"Received GET request for: {self.path}")
        path = self.path.split('?')[0]
        
        if path == '/' or path == '/preview_all.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self._set_cors_headers()
            self.end_headers()
            try:
                with open('preview_all.html', 'rb') as f:
                    self.wfile.write(f.read())
                print(f"Successfully served preview_all.html")
            except ConnectionAbortedError:
                print(f"Client aborted connection while serving preview_all.html")
            except Exception as e:
                print(f"Error serving preview_all.html: {str(e)}")
                try:
                    self.send_error(500, 'Internal Server Error')
                except:
                    pass
        elif path == '/api/progress':
            self._handle_get_progress()
        elif path == '/api/assessments':
            self._handle_get_assessments()
        elif path == '/api/community':
            self._handle_get_community()
        elif path == '/test_connection.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self._set_cors_headers()
            self.end_headers()
            try:
                with open('test_connection.html', 'rb') as f:
                    self.wfile.write(f.read())
                print(f"Successfully served test_connection.html")
            except ConnectionAbortedError:
                print(f"Client aborted connection while serving test_connection.html")
            except Exception as e:
                print(f"Error serving test_connection.html: {str(e)}")
                try:
                    self.send_error(500, 'Internal Server Error')
                except:
                    pass
        elif path.endswith('.css'):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self._set_cors_headers()
            self.end_headers()
            try:
                with open(path[1:], 'rb') as f:
                    self.wfile.write(f.read())
                print(f"Successfully served CSS file: {path[1:]}")
            except ConnectionAbortedError:
                print(f"Client aborted connection while serving CSS file")
            except Exception as e:
                print(f"Error serving CSS file: {str(e)}")
                try:
                    self.send_error(404, 'File not found')
                except:
                    pass
        elif path.endswith('.js'):
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self._set_cors_headers()
            self.end_headers()
            try:
                with open(path[1:], 'rb') as f:
                    self.wfile.write(f.read())
                print(f"Successfully served JS file: {path[1:]}")
            except ConnectionAbortedError:
                print(f"Client aborted connection while serving JS file")
            except Exception as e:
                print(f"Error serving JS file: {str(e)}")
                try:
                    self.send_error(404, 'File not found')
                except:
                    pass
        else:
            print(f"404 - File not found for: {self.path}")
            try:
                self.send_error(404, 'File not found')
            except:
                pass

    def do_POST(self):
        if self.path == '/execute':
            self._handle_execute_code()
        elif self.path == '/api/progress':
            self._handle_update_progress()
        elif self.path == '/api/assessments':
            self._handle_submit_assessment()
        elif self.path == '/api/community/posts':
            self._handle_create_post()
        elif self.path.startswith('/api/community/comments/'):
            self._handle_add_comment()
        else:
            try:
                self.send_error(404, 'File not found')
            except:
                pass

    def _handle_execute_code(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = json.loads(post_data.decode('utf-8'))
        
        code = post_data.get('code', '')
        if not code:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'No code provided'}).encode('utf-8'))
            return
        
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.py', delete=False) as f:
            f.write('# -*- coding: utf-8 -*-\n')
            f.write(code)
            temp_file_name = f.name
        
        try:
            result = subprocess.run(
                [sys.executable, temp_file_name],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            response = {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except ConnectionAbortedError:
            print(f"Client aborted connection during code execution")
        except subprocess.TimeoutExpired:
            self.send_response(408)
            self.send_header('Content-type', 'application/json')
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'Code execution timed out', 
                'stdout': '', 
                'stderr': 'Execution timed out after 10 seconds', 
                'returncode': 1
            }).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': str(e), 
                'stdout': '', 
                'stderr': str(e), 
                'returncode': 1
            }).encode('utf-8'))
        finally:
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)

    def _handle_get_progress(self):
        data = data_manager._read_file('progress.json')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _handle_update_progress(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        with data_manager.lock:
            progress_data = data_manager._read_file('progress.json')
            user_id = data.get('userId', 'default')
            
            if user_id not in progress_data:
                progress_data[user_id] = {
                    'sections': {},
                    'totalProgress': 0,
                    'lastUpdated': datetime.now().isoformat()
                }
            
            section = data.get('section')
            if section:
                progress_data[user_id]['sections'][section] = {
                    'completed': data.get('completed', False),
                    'progress': data.get('progress', 0),
                    'timeSpent': data.get('timeSpent', 0),
                    'lastAccessed': datetime.now().isoformat()
                }
            
            total_sections = len(progress_data[user_id]['sections'])
            completed_sections = sum(1 for s in progress_data[user_id]['sections'].values() if s.get('completed', False))
            progress_data[user_id]['totalProgress'] = (completed_sections / total_sections * 100) if total_sections > 0 else 0
            progress_data[user_id]['lastUpdated'] = datetime.now().isoformat()
            
            data_manager._write_file('progress.json', progress_data)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'progress': progress_data[user_id]}).encode('utf-8'))

    def _handle_get_assessments(self):
        data = data_manager._read_file('assessments.json')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _handle_submit_assessment(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        with data_manager.lock:
            assessments = data_manager._read_file('assessments.json')
            user_id = data.get('userId', 'default')
            
            if user_id not in assessments:
                assessments[user_id] = []
            
            assessment = {
                'id': len(assessments[user_id]) + 1,
                'quizId': data.get('quizId'),
                'score': data.get('score'),
                'total': data.get('total'),
                'answers': data.get('answers', {}),
                'timestamp': datetime.now().isoformat()
            }
            
            assessments[user_id].append(assessment)
            data_manager._write_file('assessments.json', assessments)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'assessment': assessment}).encode('utf-8'))

    def _handle_get_community(self):
        data = data_manager._read_file('community.json')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _handle_create_post(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        with data_manager.lock:
            community_data = data_manager._read_file('community.json')
            
            new_post = {
                'id': len(community_data['posts']) + 1,
                'author': data.get('author', 'Anonymous'),
                'title': data.get('title', ''),
                'content': data.get('content', ''),
                'category': data.get('category', 'general'),
                'likes': 0,
                'comments': [],
                'timestamp': datetime.now().isoformat()
            }
            
            community_data['posts'].insert(0, new_post)
            data_manager._write_file('community.json', community_data)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'post': new_post}).encode('utf-8'))

    def _handle_add_comment(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        post_id = self.path.split('/')[-1]
        
        with data_manager.lock:
            community_data = data_manager._read_file('community.json')
            
            comment = {
                'id': len(community_data.get('comments', {}).get(post_id, [])) + 1,
                'author': data.get('author', 'Anonymous'),
                'content': data.get('content', ''),
                'timestamp': datetime.now().isoformat()
            }
            
            if post_id not in community_data['comments']:
                community_data['comments'][post_id] = []
            
            community_data['comments'][post_id].append(comment)
            data_manager._write_file('community.json', community_data)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'comment': comment}).encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server running at http://localhost:{port}')
    print('Press Ctrl+C to stop server')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
from jupyter_client import KernelManager
# from baldr import Application
import asyncio
import multiprocessing


class Kernel:
    def __init__(self, **kwargs):
        self._manager = KernelManager(**kwargs)
        self._manager.start_kernel()
        self._client = self._manager.client()
        self._client.start_channels()
        self._client.wait_for_ready()

    @property
    def manager(self):
        return self._manager

    @property
    def client(self):
        return self._client

    def execute(self, msg):
        self._client.execute(msg)

        status = 'busy'
        result = None

        while status == 'busy':
            msg = self._client.get_iopub_msg(timeout=1)
            content = msg.get('content')
            msg_type = msg.get('msg_type')
            print(msg)

            # 'text/plain' in ['content']['data'] contains results from cells;
            #  'text' in ['content'] contains results from print statements
            if msg_type == 'execute_result':
                data = content.get('data')

                if data is not None:
                    result = data.get('text/plain')

            if 'execution_state' in content:
                status = msg['content']['execution_state']

        return result

    def shutdown(self):
        self._manager.shutdown_kernel()


async def _app_entry():
    kernel = Kernel(shell_port=8888)
    # app = Application()
    msg = kernel.execute("import baldr; baldr.__version__")
    print(msg)

# @click.command()
# @click.option('--start')
# def start():
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()

#     try:
#         asyncio.ensure_future(_app_entry())
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         print("Closing loop")
#         loop.close()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print("HELLO WROLD")
        # kernel = Kernel(shell_port=8888)
    print("Creating manager")
    manager = KernelManager(shell_port=8888)
    manager.start_kernel()

    print("Creating client")
    client = manager.client()
    print("Starting channels")
    client.start_channels()
    print("Wait for ready")
    client.wait_for_ready()

    print("KERNEL STARTED")
    msg = client.execute("import baldr; baldr.__version__")
    print("MESSAGE", msg)

# app = Application()
# msg = kernel.execute("import baldr; baldr.__version__")
# print("MESSAGE", msg)

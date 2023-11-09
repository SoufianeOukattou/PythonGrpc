import grpc
import math_operations_pb2
import math_operations_pb2_grpc

def run():
    # Connect to the gRPC server (replace 'localhost' and the port with your server details)
    channel = grpc.insecure_channel('localhost:50051')

    # Create a gRPC stub
    stub = math_operations_pb2_grpc.MathServiceStub(channel)

    # Input values from the user
    factorial_number = int(input("Enter a number to calculate its factorial: "))
    power_base = int(input("Enter the base for the power operation: "))
    power_exponent = int(input("Enter the exponent for the power operation: "))

    # Test the factorial operation
    factorial_request = math_operations_pb2.FactorialRequest(number=factorial_number)
    factorial_response = stub.CalculateFactorial(factorial_request)
    print(f"Factorial of {factorial_number} is: {factorial_response.result}")

    # Test the power operation
    power_request = math_operations_pb2.PowerRequest(base=power_base, exponent=power_exponent)
    power_response = stub.CalculatePower(power_request)
    print(f"{power_base} raised to the power of {power_exponent} is: {power_response.result}")

if __name__ == '__main__':
    run()

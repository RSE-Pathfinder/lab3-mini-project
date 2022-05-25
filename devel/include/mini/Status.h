// Generated by gencpp from file mini/Status.msg
// DO NOT EDIT!


#ifndef MINI_MESSAGE_STATUS_H
#define MINI_MESSAGE_STATUS_H

#include <ros/service_traits.h>


#include <mini/StatusRequest.h>
#include <mini/StatusResponse.h>


namespace mini
{

struct Status
{

typedef StatusRequest Request;
typedef StatusResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Status
} // namespace mini


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::mini::Status > {
  static const char* value()
  {
    return "b594a92c01db0a8232b059d768ace0a2";
  }

  static const char* value(const ::mini::Status&) { return value(); }
};

template<>
struct DataType< ::mini::Status > {
  static const char* value()
  {
    return "mini/Status";
  }

  static const char* value(const ::mini::Status&) { return value(); }
};


// service_traits::MD5Sum< ::mini::StatusRequest> should match
// service_traits::MD5Sum< ::mini::Status >
template<>
struct MD5Sum< ::mini::StatusRequest>
{
  static const char* value()
  {
    return MD5Sum< ::mini::Status >::value();
  }
  static const char* value(const ::mini::StatusRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::mini::StatusRequest> should match
// service_traits::DataType< ::mini::Status >
template<>
struct DataType< ::mini::StatusRequest>
{
  static const char* value()
  {
    return DataType< ::mini::Status >::value();
  }
  static const char* value(const ::mini::StatusRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::mini::StatusResponse> should match
// service_traits::MD5Sum< ::mini::Status >
template<>
struct MD5Sum< ::mini::StatusResponse>
{
  static const char* value()
  {
    return MD5Sum< ::mini::Status >::value();
  }
  static const char* value(const ::mini::StatusResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::mini::StatusResponse> should match
// service_traits::DataType< ::mini::Status >
template<>
struct DataType< ::mini::StatusResponse>
{
  static const char* value()
  {
    return DataType< ::mini::Status >::value();
  }
  static const char* value(const ::mini::StatusResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MINI_MESSAGE_STATUS_H
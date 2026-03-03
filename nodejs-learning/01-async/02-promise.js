// Promise 方式 - 更清晰
function fetchUserPromise(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: `User ${id}` })
      } else {
        reject(new Error('Invalid ID'))
      }
    }, 1000)
  })
}

// 使用 .then()
console.log('开始...')

fetchUserPromise(1)
  .then(user => {
    console.log('获取到用户:', user)
    return fetchUserPromise(2) // 链式调用
  })
  .then(user2 => {
    console.log('获取到第二个用户:', user2)
  })
  .catch(err => {
    console.error('错误:', err.message)
  })

console.log('请求已发出...')
